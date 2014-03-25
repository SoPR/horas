# TO-DO

Sorry for the spanglish. If you want to contribute just pick a task and update it's status, make sure you add your GitHub username so we can get in touch.


- :white_check_mark: - Initial social auth setup with Twitter, Facebook, Google and Mozilla Persona.

- :white_check_mark: - Setup of Brunch With Ember Reloaded.

- :white_check_mark: - Replace Ember.js setup with something minimal. We made the decision to keep the app a "plain-old Django app". This should extend the amount of local contributors.

- :white_check_mark: - Override all auth templates with our custom versions.

- :white_check_mark: - Create django apps and urls for development.

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


- :white_check_mark: - Build templates / css based on [current wireframes](https://github.com/SoPR/horas/tree/design).

- :white_check_mark: - Come up with a name and domain for the project. Please join the discussion on [issue #1](https://github.com/SoPR/horas/issues/1).

- :white_check_mark: - Expertise tags. Every user should be able to add a bunch of tags which describe the topics she is good at. This information will be used to search for users in a specific topic.

- :white_check_mark: - Create `Meeting` model to keep track of future meetings and it's status.
    - This model will reference a `mentor` and a `protege`, it will have a `DateTime`, a `format` (Skype, Hangout, Phone) and a status (`scheduled`, `cancelled`). We are going to need a `cancelled_by` field to record who cancelled the meeting). Meeting creation will be done via a weekly scheduled job that will create all the available meetings for the next week. The idea is that every Monday at 9AM we create all the meeting slots for the following week. Every user will only have 1 meeting spot available per week.

- :white_check_mark: - Profile view should display an "Edit Profile" button to the profile owner.

- **[not started]** - Profile view should display a list of all meetings that user has scheduled as a mentor of apprentice.

- **[not started]** - User should be able to cancel a meeting by going to his/her profile and clicking the "Cancel Meeting" button.

- :white_check_mark: - Cancelling a meeting should trigger the creation of a new meeting slot for the host of the meeting.

- **[not started]** - We need to setup something like Celery or simpler if possible to handle async operations like email notifications.

- **[not started]** - Write HTML and plain text templates for email notifications

- **[in progress: crm114]** - User should receive email notification when
    - :white_check_mark: Meeting slots are created
    - :white_check_mark: Meeting is reserved / scheduled
    - :white_check_mark: Meeting is cancelled
    - 24 hrs before the meeting starts
    - 3 hrs after the meeting start time to ask for feedback

- **[not started]** - Add and configure DjangoRESTFramework to add a full REST API to the site using Sessions, oAuth2 and JWT (with user initiated expiration enabled) for auth. Make sure we are integrating correctly with allauth.

- :white_check_mark: - Implement Search and Search Results page

- **[in progress: crm114]** - Create a CONTRIBUTING.md file explaning how to contribute to the project. The document should have sections for developers, designers and everyone else. We can [use this as a guide](https://github.com/TryGhost/Ghost/blob/master/CONTRIBUTING.md).

- **[in progress: crm114]** - Create an AUTHORS.md file for listing all contributors for the project. We can [use this as a guide](https://github.com/kennethreitz/requests/blob/master/AUTHORS.rst).

- **[not started]** - Signup flow: After user sign up from social media providers we must redirect the user to a form asking for all the required information like first and last name, email, bio ,etc. Some providers don't have all this info. We must also give the user a chance to connect more social networks to the account. Finally the user must choose their prefered "meeting hours".

- **[not started]** - Hide header when user is not authenticated. Also define what to show, maybe a call to action.

- **[not started]** - When the user has no available meetings what should we show? maybe a call to action to "subscribe" to that user, so when new meetings are available you get a notification.

- **[not started]** - Migrate settings.py setup to use [jezdez/django-configurations](https://github.com/jezdez/django-configurations/). We can use [this example](https://gist.github.com/jpadilla/864f53b67efaf1c1dd1c) as a reference.

- **[in progress: crm114]** - Setup and deploy [comunidad.1hora.org](http://comunidad.1hora.org) using [Discourse](http://www.discourse.org/). The idea is to have a place where people can share conversations around what happens on 1hora.org. Somewhere to go and talk about their 1hora.org experiences. 
