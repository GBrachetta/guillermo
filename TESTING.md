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
  - [Bag App](#bag-app)
  - [Checkout app](#checkout-app)
- [Validators and linters](#validators-and-linters)
- [Issues and bugs](#issues-and-bugs)
  - [Manually accessing `contact/` from the URL](#manually-accessing-contact-from-the-url)
  - [Contact from](#contact-from)
  - [Modals within for loops](#modals-within-for-loops)
  - [Parallax Home app](#parallax-home-app)
  - [Webhooks on localhost](#webhooks-on-localhost)
  - [GSAP animations and landscape phones](#gsap-animations-and-landscape-phones)
  - [Validation in quantity input form](#validation-in-quantity-input-form)

Testing was performed manually exhaustively, putting the app under sufficient stress to consider it solid and stable.

## Responsiveness

> - *As a user I would like to have a pleasant experience in whichever device I use so I can visit regardless of where I do it from.*

### Navbar

- **User stories tested**

> - *As a user I would like to navigate the site easily so I can quickly find what I look for.*
> - *As a user I would like to see clearly what's in my shopping bag at all times so I don't forget to checkout.*

- **Tests performed**
  - Click on all the nav links and make sure they all point to the desired destination.
    - *Verdict: Passed.* :white_check_mark:
  - Check navbar on different devices and make sure it collapses when required.
    - *Verdict: Passed.* :white_check_mark:
  - Make sure that both dropdown menus (hamburger and profile) scroll smoothly on all devices and close when clicked outside of them.
    - *Verdict: Passed.* :white_check_mark:
  - Make sure that navbar is visible at all times on all devices.
    - *Verdict: Passed.* :white_check_mark:
  - Check that nav links react on hover changing their colour.
    - *Verdict: Passed.* :white_check_mark:
  - Check if the class passed from the views makes the current nav link active in order to indicate the user where they are currently on.
    - *Verdict: Passed.* :white_check_mark:
  - Check if an authenticated user sees their username instead of "profile" and if they have access to functionalities reserved to logged in users.
    - *Verdict: Passed.* :white_check_mark:
  - Check if admins have management options available when logged in.
    - *Verdict: Passed.* :white_check_mark:
  - Check if there're items in the bag by having a visual indication, both when expanded and when collapsed.
    - *Verdict: Passed.* :white_check_mark:

### Footer

- **User stories tested**

> - *As a user I would like to easily find social media links so I can quickly explore further.*
> - *As a user I would like to always have access to contact information so I can get in touch from whichever page I'm in.*
> - *As a user I would like to know his biography and experience so I know what supports his art.*
> - *As a user I would like to know who the artist is so I can feel connected to them.*

- **Tests performed**

- Social icons redirect to the corresponding profiles in a blank page.
  - *Verdict: Passed.* :white_check_mark:
- Footer is visible, fixed to bottom and present on all pages.
  - *Verdict: Passed.* :white_check_mark:
- Clicking on the email (contact) link opens a modal with a form to send a message.
  - *Verdict: Passed.* :white_check_mark: :star:
- The contact form is accessible from any page of the site.
  - *Verdict: Passed.* :white_check_mark:
- The form populates correctly user information if the user is authenticated.
  - *Verdict: Passed.* :white_check_mark:
- The form is responsive and works as desired on all sizes and devices.
  - *Verdict: Passed.* :white_check_mark:
- The user receives a notification upon an email has been sent successfully.
  - *Verdict: Passed.* :white_check_mark:
- The footer accommodates to different devices and stacks its content accordingly.
  - *Verdict: Passed.* :white_check_mark:

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
  - *Verdict: Passed.* :white_check_mark: :star:
- The overlay content ove the images animates and fades in correctly on all devices.
  - *Verdict: Passed.* :white_check_mark:
- Text is readable on all platforms.
  - *Verdict: Passed.* :white_check_mark:
- The modal with the biography performs as expected on all platforms and is clear to read.
  - *Verdict: Passed.* :white_check_mark:
- The parallax works correctly.
  - *Verdict: Passed.* :white_check_mark:
- The overlays animate opacity correctly.
  - *Verdict: Passed.* :white_check_mark:

### Events App

> - *As a user I would like to be able to easily find information about events so I can plan attending one.*
> - *As a user I would like to be able to add events so they display automatically on my site in the right order.*
> - *As a user I would like to be able to modify events so they update automatically on my site in the right order.*
> - *As a user I would like to be able to delete events so they disappear automatically from my site.*

- Events automatically find their way to the corresponding grid: if events are future they render in the `Upcoming Events` grid, arranged from sooner to later in time, si the user can quickly find the next activities.
  - *Verdict: Passed.* :white_check_mark:
- likewise, when the event is in the past, they render in the `Past Events` grid, in this case organised from most recent to farthest in time (reversed) so the user can quickly see what were his most recent activities.  
  - *Verdict: Passed.* :white_check_mark:
- Events change from one grid to the other automatically, so the user only has to input the event once and forget about them.  
  - *Verdict: Passed.* :white_check_mark:
- Links to the venues function correctly and open a blank page.
  - *Verdict: Passed.* :white_check_mark:
- Grids have a completely different layout depending on screen size, and the information is always clear and efficiently transmitted.
  - *Verdict: Passed.* :white_check_mark:
- Administrators can edit an event when they are logged in by clicking on the icon displaying exclusively to them.
  - *Verdict: Passed.* :white_check_mark:
- Administrators can delete an event when they are logged in by clicking on the icon displaying exclusively to them. Clicking on the delete icon brings up a modal requesting confirmation. Modals within for loops were a successfully sorted challenge and the implementation works perfectly and faultlessly.
  - *Verdict: Passed.* :white_check_mark: :star:

### Album App

> - *As a user I would like to be able to see what their looks are so I can recognise him.*
> - *As a user I would like to be able to add media and have it automatically added to my album so I don't need extra effort.*
> - *As a user I would like to be able to edit media so it automatically updates my album.*
> - *As a user I would like to be able to delete media so it automatically disappears from my album.*
> - *As a user I would like to be able to replace photos and have a preview of it so I don't make mistakes.*

- The gallery works responsively across all systems.
  - *Verdict: Passed.* :white_check_mark:
- Lightbox displays extra information about the images (title, caption)
  - *Verdict: Passed.* :white_check_mark:
- Images can be shared from the lightbox, via a direct link or social media.
  - *Verdict: Passed.* :white_check_mark:
- Images can be downloaded at full resolution.
  - *Verdict: Passed.* :white_check_mark:
- Album can be updated by admins and the additions or modifications take place instantly and without further action required.
  - *Verdict: Passed.* :white_check_mark:
- Images can be individually edited, name and caption changed and image replaced and these changes take place
seamlessly and without further action required.
  - *Verdict: Passed.* :white_check_mark:
- Gallery generates randomly and creates a different layout on every reload automatically.
  - *Verdict: Passed.* :white_check_mark:
- Video plays in the lightbox.
  - *Verdict: Passed.* :white_check_mark:
- Video thumbnails are generated automatically.

### Profiles app

> - *As a user I would like to be able to register an account so I can make effortless future purchases.*
> - *As a user I would like to be able to reset my password so I can log in in case I forgot it.*
> - *As a user I would like to be able to see my order history so I can make sure to know what I have purchased.*
> - *As a user I would like to be able to update my user details so I can be sure my delivery information is accurate.*

- Account is created and user receives notification email requesting to confirm email address automatically.
  - *Verdict: Passed.* :white_check_mark:
- Activation link received by email works to effectively confirm email address, allowing to log in.
  - *Verdict: Passed.* :white_check_mark:
- Users receive a reset password link via email when requested.
  - *Verdict: Passed.* :white_check_mark:
- Users can alter and update their delivery information and all information related to their account, excepting username.
  - *Verdict: Passed.* :white_check_mark:
- Users can add, change or delete email addresses and manage them, changing which one is the primary one (and thus receiving communications through that primary one).
  - *Verdict: Passed.* :white_check_mark:
- Users can change their password.
  - *Verdict: Passed.* :white_check_mark:
- Users have an overview of their order history, ordered from the more recent, and can access individual orders in a clear way.
  - *Verdict: Passed.* :white_check_mark:
- Users can log out with one click without needing to go over the intermediary "Confirm Logout" form. This was achieved by adding the variable `ACCOUNT_LOGOUT_ON_GET = True` to the settings.
  - *Verdict: Passed.* :white_check_mark:

### Shop App

> - *As a user I would like to be able to see what CDs has the artist recorded so I can decide a purchase.*
> - *As a user I would like to be able to add new items to my shop so they populate it automatically without breaking the layout.*
> - *As a user I would like to be able to edit existing items in my shop so they reflex the changes automatically.*
> - *As a user I would like to be able to delete existing items in my shop so they disappear from the shop without breaking the layout.*
> - *As a user I would like to be able to replace photos and have a preview of it so I don't make mistakes.*

- Users see a responsive grid with clear information about the products available for purchase.
  - *Verdict: Passed.* :white_check_mark:
- Navigation is intuitive and provides unequivocal options to find out more information about individual items, by clicking on the image or the button with the legend "Details".
  - *Verdict: Passed.* :white_check_mark:
- Visual clues work well on all devices and layouts by displaying an overlay on the images, inviting the user to click on them.
  - *Verdict: Passed.* :white_check_mark:
- The button "Add to Bag" effectively adds a single unit of the product to the shopping bag.
  - *Verdict: Passed.* :white_check_mark:
- Administrators can effectively edit the product from the details page, and all changes take place immediately.
  - *Verdict: Passed.* :white_check_mark:
- Administrators can effectively delete a product from the shop, a confirmation modal displays warning them of the action about to be performed for extra safety.
  - *Verdict: Passed.* :white_check_mark:
- Modal works on all layouts.
  - *Verdict: Passed.* :white_check_mark:

### Bag App

- Shopping bag can be adjusted, quantity updated and products deleted from the bag.
  - *Verdict: Passed.* :white_check_mark:
- Delivery cost information updates accordingly and it's easy to find.
  - *Verdict: Passed.* :white_check_mark:
- Subtotal and totals update and are clear.
  - *Verdict: Passed.* :white_check_mark:
- If the user decides to delete an item from their bag, a modal pops up requesting confirmation.
  - *Verdict: Passed.* :white_check_mark:
- Quantity form works as expected in adding the desired amount of items to the bag from the product detail page.
  - *Verdict: Passed.* :white_check_mark:

### Checkout app

> - *As a user I would like to be able to purchase securely the CDs so I feel peace of mind about my personal information.*

- Invalid information (i.e. wrongly formatted email, empty required fields, etc) is correctly validated and displays warnings as expected.
  - *Verdict: Passed.* :white_check_mark:
- Test credit card numbers (`4242 4242 4242 4242` for USA or any other provided for testing purposes) effectively succeeds on Stripe's side and webhooks return a success message, allowing for the order to be created and entered in the system.
  - *Verdict: Passed.* :white_check_mark:
- A confirmation email with all order information is successfully sent to the customer via my SMTP server.
  - *Verdict: Passed.* :white_check_mark:
- An additional email formatted differently is successfully delivered to the admins announcing them about the creation of a new order.
  - *Verdict: Passed.* :white_check_mark:
- The hyperlinks to view past orders display correctly and redirects to a template with information about that particular order.
  - *Verdict: Passed.* :white_check_mark:

## Validators and linters

The following validators and linters were used either remotely or with their plugins for Visual Studio Code:

- [W3C HTML Validator](https://validator.w3.org/)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - Validators and linters were used to ensure code is valid.
  - Warnings or errors only showed for jinja specific code, which is not interpreted by these validators and have been thud ignored after carefully checking them.
- [CSS Lint](http://csslint.net/)
  - I used Sass to compile my main CSS file.
  - To compile my CSS file I used [Live Sass Compiler](https://github.com/ritwickdey/vscode-live-sass-compiler) on VS Code, which saved time and ensured all rules are valid.
  - Sass allowed me to have my rules organised in different files and ensured that the resulting compiled file has no errors.
  - Sass also allowed me to automatically compile a minified file, thus saving loading time.
- [JSHint](https://jshint.com/)
  - All JS has been minified to reduce loading times, having been previously linted and free of errors.
  - No console warnings or errors are displayed at any moment.
- [PEP8](http://pep8online.com/)
- [BLACK](https://pypi.org/project/black/)
  - Both linters were used throughout development, alternating between them for extra security and double checking.
  - Both extensions were installed in my virtual environment, allowing me to spot warnings and errors instantly, and to correct them.
  - No Python warnings or errors occur.

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

- *Verdict: Passed.* :white_check_mark: :star:

### Contact from

Because the `contact` view has no template but just a modal without inheritance, the modal wouldn't render the form and an empty one was displayed.
To solve this, the following script was put in place:

```js
$(function () {
    $("#trigger-contact").on("click", () => {
        $("#form-modal").load("/contact", () => {
            $("#contact").modal("show");
        });
    });
});
```

This script loads the form from the view and places it on the modal, solving the issue satisfactory.

- *Verdict: Passed.* :white_check_mark:

### Modals within for loops

Confirmation modals to delete a record within a forloop are not so straightforward.
I considered leaving that extra security feature aside, assuming the admins would be responsible enough to think carefully before hitting a "delete" button without having a chance to regret it, but ultimately thought that wasn't a fair thing to do and decided to implement this extra feature. Here's how I approached it:
The link to the modal includes a `forloop.counter` in its `data-target` attribute, and the modal's `id` has the same information in it, making thus certain that the modal to confirm a deletion will be in the correct iteration of the loop.
From that point I put in place the following script that made possible to execute a post request with the given data, making the `csrftoken` match the information from the `csrfmiddlewaretoken` so the post request could succeed:

```js
$(".remove-button").on("click", function (e) {
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let itemId = $(this).attr("class").split("remove_")[1];
    let url = `/album/delete_media/${itemId}/`;
    let data = {
        csrfmiddlewaretoken: csrfToken,
    };

    $.post(url, data).done(function () {
        location.reload();
    });
});
```

Where `remove-button` is a class of the delete button in the modal, takes the value of the `csrfmiddlewaretoken`, takes the id by splitting it from the class and declares the delete url.
Finally, JQuery makes a post request with on that url with the corresponding `csrftoken` and reloads the page.

- *Verdict: Passed.* :white_check_mark: :star:

### Parallax Home app

I found an unexpected issue when discovered that iOS looks at `viewport` in a unique way, taking into account for it all html content rather than just the visible space.
That's why it is so tricky to use `background-image: cover` on iOS.
On my homepage I have 4 dives stacked displaying each a cover background image, and while it worked smoothly on all platforms, on iOS it resulted in a very zoomed in image covering each one of those divs, thus resulting in a far from ideal situation.
This issue is normally sorted by using `background-attachment: scroll` instead of `fixed` on iOS, but that didn't work for my situation because I have in place a parallax scrolling all backgrounds at a different rathe than the general scrolling itself, and using the `scroll` method creates a blank gap between the four divs.
I finally used a combination of [parallax.js](https://pixelcog.github.io/parallax.js/) and [GSAP](https://greensock.com/gsap/), the former to deal with background images assigning them as image tags, and the latter to deal with the opacity of overlays and the translating content animations.
The result is a great compromise, displaying as expected on desktops and only sacrificing the parallax on iOS but retaining the background image sizes and aspect ratios. Additionally, GSAP's animations of overlays and opacity and movement of text works great across all platforms.

- *Verdict: Fixed - Passed.* :white_check_mark: :star: :sparkles:

### Webhooks on localhost

Testing [Stripe](https://stripe.com/en-nl)'s webhooks while working locally rather than on GitPod wasn't so readily clear at first. In order to make webhooks work and be able to test their functionality I tunneled my local IP and port to Stripe using [Ngrok](https://ngrok.com/), which allowed me to do just that.
I obviously needed to allow my Ngrok tunnel address in my project settings, and since that address is dynamically created I had to do that on every occasion, also creating a new webhook listener for each one of those tunnels.
It finally served the purpose perfectly and that allowed me to test and succeed setting up my Stripe webhooks.

- *Verdict: Fixed - Passed.* :white_check_mark:

### GSAP animations and landscape phones

Full size screen parallax with a visible navbar doesn't perform well on **phone in landscape position**, and at the moment of this writing I'm considering a number of options to deal with it, but I don't want to sacrifice an otherwise perfectly functional and beautiful layout for the very rare user willing to try parallax on phone in landscape.
Some of the options being considered at the moment of this writing are:

- Having an alternative set of CSS rules for users rotating their phones on the homepage. The objections to this are:
  - The procedure can produce unexpected results as each OS is susceptible of treating those rules differently.
  - Some computers could show those sets of rules since computer screens are landscape.
  - Tablets will suffer from the experience, not having being able to enjoy the experience they would without those queries.

- Hiding the navbar on landscape.
  - Again, a far from ideal solution and very unfriendly and counterintuitive.

- *Verdict: under investigation.* :microscope:

### Validation in quantity input form

There was an issue on the form to update the quantity of items in the shopping bag, which allowed to manually enter a number outside the values permitted and still submit the form. With a sufficiently large value that would return a server error on checkout.
Albeit a non-critical issue, I decided to be defensive, and the following method was used:

- I identified which iteration of the forloop was the input referring to by using `{{ forloop.counter }}` in the form id.
- I also used the same counter on the button updating the form.
- Eventually, JQuery reads that information on click and attempts to validate the form.
- if the form validates, it submits.
- in case it doesn't, it displays a validation error letting the user know that the value is not allowed and the form isn't submitted.

- *Verdict: Fixed - Passed.* :white_check_mark:
