'use strict';

module.exports = App.Router.map(function() {
    // this.resource('about');
});

App.Router.reopen({
    location: 'history'
});
