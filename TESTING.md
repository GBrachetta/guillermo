# Back to [README](README.md) <!-- omit in toc -->

- [Responsiveness](#responsiveness)
  - [Navbar](#navbar)
  - [Footer](#footer)
  - [General responsiveness](#general-responsiveness)
- [Apps](#apps)
  - [Home App](#home-app)
  - [Events App](#events-app)
  - [Album App](#album-app)
  - [Profiles app](#profiles-app)
  - [Shop App](#shop-app)
  - [Checkout app](#checkout-app)
  - [Bag App](#bag-app)
- [Validators and linters](#validators-and-linters)
- [Issues and bugs](#issues-and-bugs)
  - [Manually accessing `contact/` from the URL](#manually-accessing-contact-from-the-url)
  - [Contact from](#contact-from)
  - [Modals within for loops](#modals-within-for-loops)
  - [Parallax Home app](#parallax-home-app)
  - [Webhooks on localhost](#webhooks-on-localhost)
  - [GSAP animations and landscape phones](#gsap-animations-and-landscape-phones)

Testing was performed manually exhaustively, putting the app under sufficient stress to consider it solid and stable.

## Responsiveness

> - *As a user I would like to have a pleasant experience in whichever device I use so I can visit regardless of where I do it from.*

### Navbar

- **User stories tested**

> - *As a user I would like to navigate the site easily so I can quickly find what I look for.*
> - *As a user I would like to see clearly what's in my shopping bag at all times so I don't forget to checkout.*

- **Tests performed**
  - Click on all the nav links and make sure they all point to the desired destination.
    - *Verdict: passed.* :white_check_mark:
  - Check navbar on different devices and make sure it collapses when required.
    - *Verdict: passed.* :white_check_mark:
  - Make sure that both dropdown menus (hamburger and profile) scroll smoothly on all devices and close when clicked outside of them.
    - *Verdict: passed.* :white_check_mark:
  - Make sure that navbar is visible at all times on all devices.
    - *Verdict: passed.* :white_check_mark:
  - Check that nav links react on hover changing their colour.
    - *Verdict: passed.* :white_check_mark:
  - Check if the class passed from the views makes the current nav link active in order to indicate the user where they are currently on.
    - *Verdict: passed.* :white_check_mark:
  - Check if an authenticated user sees their username instead of "profile" and if they have access to functionalities reserved to logged in users.
    - *Verdict: passed.* :white_check_mark:
  - Check if admins have management options available when logged in.
    - *Verdict: passed.* :white_check_mark:
  - Check if there're items in the bag by having a visual indication, both when expanded and when collapsed.
    - *Verdict: passed.* :white_check_mark:

### Footer

- **User stories tested**

> - *As a user I would like to easily find social media links so I can quickly explore further.*
> - *As a user I would like to always have access to contact information so I can get in touch from whichever page I'm in.*
> - *As a user I would like to know his biography and experience so I know what supports his art.*
> - *As a user I would like to know who the artist is so I can feel connected to them.*

- **Tests performed**

- Social icons redirect to the corresponding profiles in a blank page.
  - *Verdict: passed.* :white_check_mark:
- Footer is visible, fixed to bottom and present on all pages.
  - *Verdict: passed.* :white_check_mark:
- Clicking on the email (contact) link opens a modal with a form to send a message.
  - *Verdict: passed.* :white_check_mark: :star:
- The contact form is accessible from any page of the site.
  - *Verdict: passed.* :white_check_mark:
- The form populates correctly user information if the user is authenticated.
  - *Verdict: passed.* :white_check_mark:
- The form is responsive and works as desired on all sizes and devices.
  - *Verdict: passed.* :white_check_mark:
- The user receives a notification upon an email has been sent successfully.
  - *Verdict: passed.* :white_check_mark:
- The footer accommodates to different devices and stacks its content accordingly.
  - *Verdict: passed.* :white_check_mark:

### General responsiveness

## Apps

### Home App

> - *As a user I would like to be visually engaged when I land on the site so I desire to stay.*
> - *As a user I would like to be able to see them in photo and video so I can know what they look like.*
> - *As a user I would like to be able to listen to what they do so I know their artistry.*
> - *As a user I would like to know what they thinks about being an artist so I can feel related as a person.*
> - *As a user I would like to know when and were have them performed before so I know their experience.*

- The images cover all viewport on all devices, are stacked correctly and are of correct proportions.
  - *Note*: iOS has a different approach to background images covering the viewport. Thanks to the use of a combination of GSAP and parallax.js this issue has been satisfactorily resolved. In the event of an iOS device visiting, overlays and content animates correctly. More importantly, images are displayed at the correct size rather than clipped and zoomed in (iOS considers 'viewport' all content rather than just the visible available space). The sacrifice to make is to renounce to the asynchronous parallax on iOS devices, a solution I consider highly satisfactory for what I get in exchange: great image placement, sizing, and animations.
  - *Verdict: passed.* :white_check_mark: :star:
- The overlay content ove the images animates and fades in correctly on all devices.
  - *Verdict: passed.* :white_check_mark:
- Text is readable on all platforms.
  - *Verdict: passed.* :white_check_mark:
- The modal with the biography performs as expected on all platforms and is clear to read.
  - *Verdict: passed.* :white_check_mark:
- The parallax works correctly.
  - *Verdict: passed.* :white_check_mark:
- The overlays animate opacity correctly.
  - *Verdict: passed.* :white_check_mark:

### Events App

> - *As a user I would like to be able to easily find information about events so I can plan attending one.*
> - *As a user I would like to be able to add events so they display automatically on my site in the right order.*
> - *As a user I would like to be able to modify events so they update automatically on my site in the right order.*
> - *As a user I would like to be able to delete events so they disappear automatically from my site.*

- Events automatically find their way to the corresponding grid: if events are future they render in the `Upcoming Events` grid, arranged from sooner to later in time, si the user can quickly find the next activities.
  - *Verdict: passed.* :white_check_mark:
- likewise, when the event is in the past, they render in the `Past Events` grid, in this case organised from most recent to fartherst in time (reversed) so the user can quickly see what were his most recent activities.  
  - *Verdict: passed.* :white_check_mark:
- Events change from one grid to the other automatically, so the user only has to input the event once and forget about them.  
  - *Verdict: passed.* :white_check_mark:
- Links to the venues function correctly and open a blank page.
  - *Verdict: passed.* :white_check_mark:
- Grids have a completely different layout depending on screen size, and the information is always clear and efficiently transmitted.
  - *Verdict: passed.* :white_check_mark:
- Administrators can edit an event when they are logged in by clicking on the icon displaying exclusively to them.
  - *Verdict: passed.* :white_check_mark:
- Administrators can delete an event when they are logged in by clicking on the icon displaying exclusively to them. Clicking on the delete icon brings up a modal requesting confirmation. Modals within for loops were a successfully sorted challenge and the implementation works perfectly and faultlessly.
  - *Verdict: passed.* :white_check_mark: :star:

### Album App

> - *As a user I would like to be able to see what their looks are so I can recognise him.*
> - *As a user I would like to be able to add media and have it automatically added to my album so I don't need extra effort.*
> - *As a user I would like to be able to edit media so it automatically updates my album.*
> - *As a user I would like to be able to delete media so it automatically disappears from my album.*
> - *As a user I would like to be able to replace photos and have a preview of it so I don't make mistakes.*

### Profiles app

> - *As a user I would like to be able to register an account so I can make effortless future purchases.*
> - *As a user I would like to be able to reset my password so I can log in in case I forgot it.*
> - *As a user I would like to be able to see my order history so I can make sure to know what I have purchased.*
> - *As a user I would like to be able to update my user details so I can be sure my delivery information is accurate.*

### Shop App

> - *As a user I would like to be able to see what CDs has the artist recorded so I can decide a purchase.*
> - *As a user I would like to be able to add new items to my shop so they populate it automatically without breaking the layout.*
> - *As a user I would like to be able to edit existing items in my shop so they reflex the changes automatically.*
> - *As a user I would like to be able to delete existing items in my shop so they disappear from the shop without breaking the layout.*
> - *As a user I would like to be able to replace photos and have a preview of it so I don't make mistakes.*

### Checkout app

> - *As a user I would like to be able to purchase securely the CDs so I feel peace of mind about my personal information.*

### Bag App

## Validators and linters

The following validators and linters were used either remotely or with their plugins for Visual Studio Code:

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [CSS Lint](http://csslint.net/)
- [JSHint](https://jshint.com/)
- [PEP8](http://pep8online.com/)
- [BLACK](https://pypi.org/project/black/)

## Issues and bugs

### Manually accessing `contact/` from the URL

The hyperlink that displays the modal with the biography from the footer lives in a view in the main app. Since the modal has an `href="#"`, accessing the view directly by entering it in the address bar would render an unformatted modal (they don't use template inheritance). To prevent this very rare occurrence, the following JS script has been put in place in the event an user entered the url manually in the address bar:

```js
if (window.location.href.indexOf("contact") > -1) {
        window.location.replace("https://guillermo-brachetta.herokuapp.com");
    }
```

This script is plain JS, since the modal, for not having any inheritance, doesn't load JQuery at when rendered directly.
The script redirects to the home page, thus avoiding rendering an unformatted template in the very unlikely event of an user entering the address purposely.

- *Verdict: passed.* :white_check_mark: :star:

### Contact from

### Modals within for loops

### Parallax Home app

### Webhooks on localhost

### GSAP animations and landscape phones
