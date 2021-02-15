# Link Shortener

Static link shortener service built for my GitHub Pages powered custom domain.

Supports password protected links (with AES + PBKDF2 encryption)

> Read More: [Blog Post](https://featherbear.cc/blog/post/featherbear.cc-go/)

---

When pushed to GitHub, the GitHub Workflow actions will automatically build and publish files to the `gh-pages` branch. Ensure that `gh-pages` is being served in your repository settings

## Configuration

Rename the `links.json.example` file to `links.json` and add modify as per the example links.

To modify the HTML templates, edit the `template.html`, `template_password.html` and `public/404.html` files.

## License

Copyright © 2021 Andrew Wong

This software is licensed under the MIT License.
You are free to redistribute it and/or modify it under the terms of the license.
