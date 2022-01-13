## Welcome to GitHub Pages

[Go to the first page](/first_page.md)

You can use the [editor on GitHub](https://github.com/caigun/caigun.blog/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)


def hanoi(from_rod, to_rod, help_rod, n):
    if n==1:
        print("move from",from_rod,"to",to_rod)
    else:
        hanoi(from_rod, help_rod, to_rod, n-1)
        print("move from",from_rod,"to",to_rod)
        hanoi(help_rod, to_rod, from_rod, n-1)

hanoi('left','right','middle',5)

```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/caigun/caigun.blog/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
