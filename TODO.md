# TO-DO

Sorry for the spanglish. If you want to contribute just pick a task and update it's status, make sure you add your GitHub username so we can get in touch.


- :white_check_mark: - Initial social auth setup with Twitter, Facebook, Google and Mozilla Persona.

- :white_check_mark: - Setup of Brunch With Ember Reloaded.

- :white_check_mark: - Replace Ember.js setup with something minimal. We made the decision to keep the app a "plain-old Django app". This should extend the amount of local contributors.

- :white_check_mark: - Override all auth templates with our custom versions.

- **[in progress: jpadilla]** - Create django apps and urls for development.

    - core
        - home /

    - profiles
        - user profile - /<:username>/
        - user profile edit - /<:username>/update/
        - user meetings feed - /<:username>.ics|rss|atom

    - search
        - search - /search/
        - search results page - /search?q=<:searchterms>

    - meetings
        - confirmation - /meeting/<:meeting_id>/


- **[in progress: gcollazo]** - Build templates based on [current wireframes](https://github.com/SoPR/horas/tree/design).

- **[in progress: community]** - Come up with a name and domain for the project. Please join the discussion on [issue #1](https://github.com/SoPR/horas/issues/1).

- :white_check_mark: - Expertise tags. Every user should be able to add a bunch of tags which describe the topics she is good at. This information will be used to search for users in a specific topic.

- **[not started]** - Create `Meeting` model to keep track of future meetings and it's status.
    - This model will reference a `mentor` and a `protege`, it will have a `DateTime`, a `format` (Skype, Hangout, Phone) and a status (`scheduled`, `cancelled`). We are going to need a `cancelled_by` field to record who cancelled the meeting). Meeting creation will be done via a weekly scheduled job that will create all the available meetings for the next week. The idea is that every Monday at 9AM we create all the meeting slots for the following week. Every user will only have 1 meeting spot available per week.

- **[not started]** - Add and configure DjangoRESTFramework to add a full REST API to the site using Sessions, oAuth2 and JWT (with user initiated expiration enabled) for auth. Make sure we are integrating correctly with allauth.

- **[not started]** - Profile view should display an "Edit Profile" button to the profile owner.

- **[not started]** - Profile view should display a list of all meetings that user has scheduled as a mentor of apprentice.

- **[not started]** - User should be able to cancel a meeting by going to his/her profile and clicking the "Cancel Meeting" button. This action should trigger the creation of a new meeting slot for the host of the meeting.

- **[not started]** - We need to setup something like Celery or simpler if possible to handle async operations like email notifications.

- **[not started]** - User should receive email notification when
    - Meeting slots are created
    - Meeting is reserved / scheduled
    - Meeting is cancelled
    - 24 hrs before the meeting starts
    - 3 hrs after the meeting start time to ask for feedback


