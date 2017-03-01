# Newsletter

[![](https://img.shields.io/badge/made%20by-Protocol%20Labs-blue.svg?style=flat-square)](http://ipn.io)
[![](https://img.shields.io/badge/project-IPFS-blue.svg?style=flat-square)](http://ipfs.io/)
[![](https://img.shields.io/badge/freenode-%23ipfs-blue.svg?style=flat-square)](http://webchat.freenode.net/?channels=%23ipfs)

[![](https://cdn.rawgit.com/jbenet/contribute-ipfs-gif/master/img/contribute.gif)](https://github.com/ipfs/community/blob/master/contributing.md)

Prepare and store our newsletter.

- [Idea](#idea)
- [Contribute](#contribute)
- [This repo](#this-repo)
  - [Process for writing the Newsletter](#process-for-writing-the-newsletter)
  - [Styleguide & Suggestions](#styleguide-&-suggestions)

## Idea

Similar to the [Rust community's](https://this-week-in-rust.org/), we want to have a newsletter that talks about what was done in the past week by varous contributors. This will help:

- Keep people in the loop about what is going on at Protocol Labs and on IPFS.
- Tell active contributors when new versions or tools are available.
- Attribute developers who have contributed to open-source software related to IPFS.

## Contribute

The Newsletter takes a _lot of work_. This work can best be done by being distributed. If you know of anything cool that happens in a given week, anything that other people might be excited about, add it to the newsletter by adding a comment about it to the PR or Issue for that week's newsletter.

Here are the steps to do that:
 - See something cool, or make something cool.
 - Go to the open PR for that week's newsletter.
 - Add a comment about the thing. Add a link, if possible.
 - Revel in the knowledge you are great.

Also, please help us out if you think the roundup could be better! [Open an issue!](https://github.com/ipfs/newsletter/issues/new)

## This repo

- Stores the final versions for past newsletters, posted elsewhere - the blog, email, and so on;
- Tracks issues related to the roundups in the [issues](https://github.com/ipfs/newsletter/issues/);
- Stores tools used to make the roundups


### Process for writing the Newsletter

- Open a Pull Request to create a new Markdown formatted file in the `published` folder. The naming format should be as in this example: `002-2016-jan-5.md`, for the newsletter of the sprint starting January 5th in 2016.
- Collect feedback and iterate on the draft.
- Images
  - Add files into published folder
  - Add using `-w` to ipfs
  - Use ipfs.io gateway to add files in
- Merge it after:
  - Sign off from pertinent people
  - The travis build for the branch completes after each push.
- Crosspost
  - [ipfs/ipfs#151](https://github.com/ipfs/ipfs/issues/151)
  - [the Blog](//github.com/ipfs/blog)
  - The IPFS Tinyletter, using `md2html` npm package to generate HTML
  - Twitter: post the blog link after it is merged and published.

### Styleguide & Suggestions

- Use people's GitHub handles and not their real names. Example: @RichardLitt, and not "Richard Littauer".
- Try and include everyone who has made a PR or commented on an issue. Often, issue comments are _major, pivotal_ contributions, and those should be captured!
- Highlight, don't just summarize; a lot of work may be trivial, and higher signal is better noise.
- In general, err on the side of giving credit to everyone involved. When people do the lion's share, mention them first. (Or even something like "@whyrusleeping and several others ... " if relevant. In the case of a release, you can link to the changelog which credits individually... but don't sweat this.)
- In general, try linking larger phrases instead of single words. They're easier to notice and click on links.
- In general, try highlighting _why_ something is cool. Call attention to things if
    1. it is done and people should know about
    2. there is a call to action -- opinions are needed.
    3. it is specially useful to draw attention to something in the newsletter.

