# Step 1: Commit changes to main branch
# make changes in main branch from Github Codespaces and --> `git add`, `git commit ...`, `git push origin main`

# Step 2: In GitHub CodeSpaces, install dependencies (if needed)
# pip install quarto-cli

# Step 3: Render the project (builds website + book)
quarto render

# Step 4: Copy book output to _site for deployment
mkdir -p _site/aws_cloud_technical_essentials
cp -r aws_cloud_technical_essentials_book/_book/* _site/aws_cloud_technical_essentials/

# Step 5: Publish to GitHub Pages
quarto publish gh-pages --no-prompt