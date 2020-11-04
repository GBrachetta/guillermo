# Back to [README](README.md) <!-- omit in toc -->

- [Responsiveness](#responsiveness)
- [Navbar](#navbar)
- [Footer](#footer)
- [Landing Page](#landing-page)
- [Events App](#events-app)
- [Album App](#album-app)
- [Profiles app](#profiles-app)
- [Shop App](#shop-app)
- [Checkout app](#checkout-app)
- [Bag App](#bag-app)
- [Validators and linters](#validators-and-linters)
- [Issues and bugs](#issues-and-bugs)

Testing was performed manually exhaustively, putting the app under sufficient stress to consider it solid and stable.

## Responsiveness

## Navbar

- **User story tested**

> As a user I would like to navigate the site easily so I can quickly find what I look for.

- Tests
  - Click on all the nav links and make sure they all point to the desired destination.
    - *Verdict: passed.* `:white_check_mark:`
  - Check navbar on different devices and make sure it collapses when required.
    - *Verdict: passed.* `:white_check_mark:`
  - Make sure that both dropdown menus (hamburger and profile) scroll smoothly on all devices and close when clicked outside of them.
    - *Verdict: passed.* `:white_check_mark:`
  - Make sure that navbar is visible at all times on all devices.
    - *Verdict: passed.* `:white_check_mark:`
  - Check that nav links react on hover changing their colour.
    - *Verdict: passed.* `:white_check_mark:`
  - Check if the class passed from the views makes the current nav link active in order to indicate the user where they are currently on.
    - *Verdict: passed.* `:white_check_mark:`
  - Check if an authenticated user sees their username instead of "profile" and if they have access to functionalities reserved to logged in users.
    - *Verdict: passed.* `:white_check_mark:`
  - Check if admins have management options available when logged in.
    - *Verdict: passed.* `:white_check_mark:`
  - Check if there're items in the bag by having a visual indication, both when expanded and when collapsed.
    - *Verdict: passed.* `:white_check_mark:`

## Footer

## Landing Page

## Events App

## Album App

## Profiles app

## Shop App

## Checkout app

## Bag App

## Validators and linters

The following validators and linters were used either remotely or with their plugins for Visual Studio Code:

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [CSS Lint](http://csslint.net/)
- [JSHint](https://jshint.com/)
- [PEP8](http://pep8online.com/)
- [BLACK](https://pypi.org/project/black/)

## Issues and bugs
