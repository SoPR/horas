/* imports for webpack build */

// images
require.context('./img/', true, /\.(jpe?g|png|gif|svg)$/i);

// styles
import './css/app.styl';

// js
import App from './app/index';
App();
