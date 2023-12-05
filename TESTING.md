Back to [README.md](README.md)

- [Testing](#testing)
    - [Feature testing](#feature-testing)
    - [Lighthouse performance](#lighthouse-performance)
    - [Code validation](#code-validation)
        - [HTML](#html)
        - [CSS](#css)
        - [JavaScript](#javascript)
        - [CI Python Linter](#ci-python-linter)

- [Bugs](#bugs)

## TESTING

Testing has taken place at all stages of development. Each feature has been released after it was functional.

User Stories have been tested before closure. 


### Code validation

#### HTML
Tested with [W3C Markup validation Service](https://validator.w3.org/)
<details>
<summary>HTML Validation:</summary>

- <details><summary>Home</summary><img src="assets/testing/home-html.png"></details>
- <details><summary>Catering</summary><img src="assets/testing/catering-html.png"></details>
- <details><summary>Item details</summary><img src="assets/testing/catering-item-html.png"></details>
- <details><summary>Admin Add Item</summary><img src="assets/testing/catering-add-html.png"></details>
- <details><summary>Admin Edit Item</summary><img src="assets/testing/catering-edit-html.png"></details>
- <details><summary>Admin Create Allergen</summary><img src="assets/testing/catering-allergen-html.png"></details>
- <details><summary>Bag</summary><img src="assets/testing/bag-html.png"></details>
- <details><summary>Checkout</summary><img src="assets/testing/checkout-html.png"></details>
- <details><summary>Hire Packages</summary><img src="assets/testing/hire-html.png"></details>
- <details><summary>Hire Requests</summary><img src="assets/testing/hire-request-html.png"></details>
- <details><summary>Admin Hire Requests List</summary><img src="assets/testing/hire-admin-list-html.png"></details>
- <details><summary>Profile</summary><img src="assets/testing/profile-html.png"></details>

</details>

#### CSS
Tested with [The W3C CSS Validation Service](https://jigsaw.w3.org/)
<details>
<summary>CSS Validation:</summary>

 - <details><summary>Main</summary><img src="assets/testing/w3c-css-main.png"></details>
 - <details><summary>Checkout</summary><img src="assets/testing/w3c-css-checkout.png"></details>
 - <details><summary>Hire</summary><img src="assets/testing/w3c-css-hire.png"></details>
 - <details><summary>Profile</summary><img src="assets/testing/w3c-css-profile.png"></details>

</details>

### Java Script elements
Tested with [JsHint](https://jshint.com/)

<details><summary>JsHint results</summary>
All JS elements have been included in this test with no errors, just minor warnings.
<img src="assets/testing/jshint-all-functions.png"></details>

#### Python Code
Tested with [CI Python Linter](https://pep8ci.herokuapp.com/)
<details>
<summary>Python Validation:</summary>

- <details><summary>Bag</summary>
    - contexts.py 
    <img src="assets/testing/bag-contexts.png">
    - bag_tools.py 
    <img src="assets/testing/bag-tools.png">
    - urls.py 
    <img src="assets/testing/bag-urls.png">
    - views.py 
    <img src="assets/testing/bag-views.png">
</details>

- <details><summary>Catering</summary>
    - admin.py 
    <img src="assets/testing/catering-admin.png">
    - forms.py 
    <img src="assets/testing/catering-forms.png">
    - models.py 
    <img src="assets/testing/catering-models.png">
    - contexts.py 
    <img src="assets/testing/catering-contexts.png">
    - urls.py 
    <img src="assets/testing/catering-urls.png">
    - views.py 
    <img src="assets/testing/catering-views.png">
    - widgets.py 
    <img src="assets/testing/catering-widgets.png">
</details>

- <details><summary>Checkout</summary>
    - admin.py 
    <img src="assets/testing/checkout-admin.png">
    - forms.py 
    <img src="assets/testing/checkout-forms.png">
    - models.py 
    <img src="assets/testing/checkout-models.png">
    - signals.py 
    <img src="assets/testing/checkout-signals.png">
    - urls.py 
    <img src="assets/testing/checkout-urls.png">
    - views.py 
    <img src="assets/testing/checkout-views.png">
</details>

- <details><summary>Hire</summary>
    - admin.py 
    <img src="assets/testing/hire-admin.png">
    - forms.py 
    <img src="assets/testing/hire-forms.png">
    - models.py 
    <img src="assets/testing/hire-models.png">
    - tools.py 
    <img src="assets/testing/hire-tools.png">
    - urls.py 
    <img src="assets/testing/hire-urls.png">
    - views.py 
    <img src="assets/testing/hire-views.png">
</details>

- <details><summary>Home</summary>
    - urls.py 
    <img src="assets/testing/home-urls.png">
    - views.py 
    <img src="assets/testing/home-views.png">
</details>

- <details><summary>Profile</summary>
    - urls.py 
    <img src="assets/testing/profile-urls.png">
    - views.py 
    <img src="assets/testing/profile-views.png">
    - models.py 
    <img src="assets/testing/profile-models.png">
    - forms.py 
    <img src="assets/testing/profile-forms.png">
</details>

- <details><summary>Main App: devil_on_pans </summary>
    - urls.py 
    <img src="assets/testing/main-urls.png">
    - views.py 
    <img src="assets/testing/404.png">
    - custom_storage.py 
    <img src="assets/testing/custom-storage.png">
</details>

</details>


## BUGS 

Several Bugs appeared at deployment to Heroku on various occasions, all seemed to be production and server issues related to python version and django. They have been documented in the Agile board on the go. 

- Remove button from bag does not display toast message after deployment

- Stripe payment intent is not a success after deployment, due to short time remaining will have to come back to it.


