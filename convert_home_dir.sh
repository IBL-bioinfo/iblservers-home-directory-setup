#!/bin/bash

REQUIRED_FILES=(".bashrc" ".mambarc" ".micromamba")

# Check if the correct number of arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <folder_path> <user_name> <user_group>"
    exit 1
fi

# Check if the script is being run with sudo
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script must be run with sudo."
  exit 1
fi

# Assign arguments to variables
FOLDER_PATH=$1
USER_NAME=$2
USER_GROUP=$3
TARGET_FOLDER="$FOLDER_PATH"_"$USER_NAME"


# Function to check if a directory has 700 permissions
check_directory_permissions() {
    local DIR_PATH=$1
    local EXPECTED_PERMISSIONS="700"

    # Get the current permissions of the directory
    local DIR_PERMISSIONS
    DIR_PERMISSIONS=$(stat -c "%a" "$DIR_PATH")

    # Check if the current permissions match the expected permissions
    if [ "$DIR_PERMISSIONS" == "$EXPECTED_PERMISSIONS" ]; then
        echo "The directory '$DIR_PATH' has the correct permissions: $DIR_PERMISSIONS"
    else
        echo "Error: The directory '$DIR_PATH' does not have the correct permissions. Expected: $EXPECTED_PERMISSIONS, Found: $DIR_PERMISSIONS"
        exit 1
    fi
}

# Check the permissions of the source folder
check_directory_permissions "$FOLDER_PATH"

# Print the provided arguments
echo "Folder path: $FOLDER_PATH"
echo "User name: $USER_NAME"
echo "User group: $USER_GROUP"
echo "Target folder: $TARGET_FOLDER"

# Check for specific files and folder inside the provided folder path
MISSING_ITEMS=()

for ITEM in "${REQUIRED_FILES[@]}"; do
    if [ ! -e "$FOLDER_PATH/$ITEM" ]; then
        MISSING_ITEMS+=("$ITEM")
    fi
done

# Print the results
if [ ${#MISSING_ITEMS[@]} -eq 0 ]; then
    echo "All required files and folders are present in '$FOLDER_PATH'."
else
    echo "The following required items are missing in '$FOLDER_PATH':"
    for ITEM in "${MISSING_ITEMS[@]}"; do
        echo "  - $ITEM"
    done
fi


# Copy all contents from the source folder to the target folder
echo "Copying contents from '$FOLDER_PATH' to '$TARGET_FOLDER'..."
cp -r "$FOLDER_PATH" "$TARGET_FOLDER"


# Edit the .bashrc file in the target folder
BASHRC_FILE="$TARGET_FOLDER/.bashrc"
if [ -f "$BASHRC_FILE" ]; then
    echo "Editing '$BASHRC_FILE' to update MAMBA_ROOT_PREFIX..."
    sed -i "s|^export MAMBA_ROOT_PREFIX=.*|export MAMBA_ROOT_PREFIX='/home/$USER_NAME/.micromamba'|" "$BASHRC_FILE"
    echo ".bashrc file updated successfully."
else
    echo "Error: .bashrc file not found in '$TARGET_FOLDER'."
    exit 1
fi



# Edit the .mambarc file in the target folder
MAMBARC_FILE="$TARGET_FOLDER/.mambarc"
if [ -f "$MAMBARC_FILE" ]; then
    echo "Editing '$MAMBARC_FILE' to update conda cache path..."
    sed -i "s|/vol/local/.conda_cache/.*|/vol/local/.conda_cache/$USER_NAME|" "$MAMBARC_FILE"
    echo ".mambarc file updated successfully."
else
    echo "Error: .mambarc file not found in '$TARGET_FOLDER'."
    exit 1
fi


# Change the ownership of the target folder and its contents
echo "Changing ownership of '$TARGET_FOLDER' and its contents to '$USER_NAME:$USER_GROUP'..."
chown -R "$USER_NAME:$USER_GROUP" "$TARGET_FOLDER"
if [ $? -eq 0 ]; then
    echo "Ownership changed successfully."
else
    echo "Error: Failed to change ownership."
    exit 1
fi
echo "Moving processed home directory to /home"
mv "$TARGET_FOLDER" /home/"$USER_NAME"


# DONE
echo "DONE"
