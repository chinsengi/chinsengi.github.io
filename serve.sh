#!/bin/bash

# Script to build and serve the Jekyll website locally
# This ensures the correct Ruby version is used

echo "Starting Jekyll site..."
echo "================================"

# Set Ruby 3.3 path
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# Check if Gemfile.lock exists and dependencies are installed
if [ ! -f "Gemfile.lock" ]; then
    echo "Installing dependencies..."
    bundle install
fi

# Serve the site on port 4000 (default Jekyll port)
echo ""
echo "Building and serving site..."
echo "Site will be available at: http://localhost:4000/"
echo "Press Ctrl+C to stop the server"
echo "================================"
echo ""

bundle exec jekyll serve --host localhost
