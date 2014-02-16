# TO-DO

Sorry for the spanglish. If you want to contribute just pick a task and update it's status, make sure you add your GitHub username so we can get in touch.


- :white_check_mark: - Initial social auth setup with Twitter, Facebook, Google and Mozilla Persona.

- :white_check_mark: - Setup of Brunch With Ember Reloaded.

- :white_check_mark: - Replace Ember.js setup with something minimal. We made the decision to keep the app a "plain-old Django app". This should extend the amount of local contributors.

- :white_check_mark: - Override all auth templates with our custom versions.

- **[in progress: gcollazo]** - Build templates based on [current wireframes](https://github.com/SoPR/horas/tree/design).

- **[in progress: community]** - Come up with a name and domain for the project. Please join the discussion on [issue #1](https://github.com/SoPR/horas/issues/1).

- **[not started]** - Make generic html rendered by the server to deliver all the JavaScript, css and `<noscript>` data.

- **[in progress: jpadilla]** - Expertise tags. Every user should be able to add a bunch of tags which describe the topics she is good at. This information will be used to search for users in a specific topic.

- **[not started]** Create `Meeting` model to keep track of future meetings and it's status.             
    - This model will reference a `mentor` and a `protege`, it will have a `DateTime`, a medium (Skype, Hangout, Phone) and a status (`waiting`, `confirmed`, `rejected`). La idea es que cada user va a tener unos settings en su profile que indican que día de la semana y a que hora va a estar disponible para conceder reuniones. Cuando estemos mirando el perfil de un user vamos a mostrar una lista de todos los slots disponibles y el user puede "book" ese espacio. Todos los usuarios deben compartir horas para poder "bookiar" horas de otros.

- **[not started]** Add and configure DjangoRESTFramework to add a full REST API to the site using Sessions, oAuth2 and JWT (with user initiated expiration enabled) for auth. Make sure we are integrating correctly with allauth.

- **[not started]** Home view. A view which will stat from the site like how many users, how many meetings and a few testimonials. Users should be able to sign up or login from this page using any of the available methods, currently: Twitter, Facebook, Google, Persona, internal accounts.

- **[not started]** Search. We should be able to search by name and areas of expertise (tags). This will require a search results page.

- **[not started]** Profile Detail View. This view will show a gravatar, full name, shot bio, social media links and expertise tags for each user. On the main area of this page we will show a few upcoming available slots. Each slot will have a [Book Now] button next to it.

- **[not started]** Profile Update View. This view will allow the user to connect to all available social media networks, change her meeting settings and enter usernames for skype, hangout, phone, physical address.

- **[not started]** Reply to meeting request view. In this view the mentor will reply `accept` or `reject` to all `Meeting`s with a state of `waiting`.
