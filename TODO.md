# TO-DO

Sorry for the spanglish. If you want to contribute just pick a task and update it's status, make sure you add your GitHub username so we can get in touch.

- <input type="checkbox" disabled checked> **[done]** - Initial social auth setup with Twitter, Facebook, Google and Mozilla Persona.

- <input type="checkbox" disabled checked> **[done]** - Setup of Brunch With Ember Reloaded.

- <input type="checkbox" disabled> **[in progress: [gcollazo](http://github.com/gcollazo)]** - Override all auth templates with our custom versions.

- <input type="checkbox" disabled> **[in progress: community]** - Come up with a name and domain for the project. Please join the discussion on [issue #1](https://github.com/SoPR/horas/issues/1).

- <input type="checkbox" disabled> **[not started]** - Make generic html rendered by the server to deliver all the JavaScript, css and `<noscript>` data.

- <input type="checkbox" disabled> **[not started]** - Expertise tags. Every user should be able to add a bunch of tags which describe the topics she is good at. This information will be used to search for users in a specific topic.

- <input type="checkbox" disabled> **[not started]** Create `Meeting` model to keep track of future meetings and it's status.             
    - This model will reference a `mentor` and a `protege`, it will have a `DateTime`, a medium (Skype, Hangout, Phone) and a status (`waiting`, `confirmed`, `rejected`). La idea es que cada user va a tener unos settings en su profile que indican que día de la semana y a que hora va a estar disponible para conceder reuniones. Cuando estemos mirando el perfil de un user vamos a mostrar una lista de todos los slots disponibles y el user puede "book" ese espacio. Todos los usuarios deben compartir horas para poder "bookiar" horas de otros.

- <input type="checkbox" disabled> **[not started]** Add and configure DjangoRESTFramework to add a full REST API to the site using Sessions, oAuth2 and JWT (with user initiated expiration enabled) for auth. Make sure we are integrating correctly with allauth.

- <input type="checkbox" disabled> **[not started]** Home view. A view which will stat from the site like how many users, how many meetings and a few testimonials. Users should be able to sign up or login from this page using any of the available methods, currently: Twitter, Facebook, Google, Persona, internal accounts.

- <input type="checkbox" disabled> **[not started]** Search. We should be able to search by name and areas of expertise (tags). This will require a search results page.

- <input type="checkbox" disabled> **[not started]** Profile Detail View. This view will show a gravatar, full name, shot bio, social media links and expertise tags for each user. On the main area of this page we will show a few upcoming available slots. Each slot will have a [Book Now] button next to it.

- <input type="checkbox" disabled> **[not started]** Profile Update View. This view will allow the user to connect to all available social media networks, change her meeting settings and enter usernames for skype, hangout, phone, physical address.

- <input type="checkbox" disabled> **[not started]** Reply to meeting request view. In this view the mentor will reply `accept` or `reject` to all `Meeting`s with a state of `waiting`.