# List files and folders in the repository, including their paths
echo "File Structure:"
find . -type f -not -path "./.*" | sort

# Retrieve the contents of key files
echo -e "\nContents of README.md:"
cat README.md

# Add other relevant documentation files, e.g., documentation/python_api.md
# echo -e "\nContents of documentation/python_api.md:"
# cat documentation/python_api.md

# Get the commit history of the repository
echo -e "\nCommit History:"
git log --oneline

# If the output is too long, you can limit the number of commits shown
# git log --oneline -n 10  # show the last 10 commits

# Compress the output into a single file and show the file size
output_file="project_state_$(date +"%Y%m%d%H%M%S").txt"
{
  find . -type f | sort
  echo -e "\nContents of README.md:"
  cat README.md
  # echo -e "\nContents of documentation/python_api.md:"
  # cat documentation/python_api.md
  echo -e "\nCommit History:"
  git log --oneline
} > "$output_file"

echo -e "\nProject state saved to: $output_file"
echo "File size:"
ls -lh "$output_file"
