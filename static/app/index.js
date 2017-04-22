/* imports for webpack build */

// images
require.context('./img/', true, /\.(jpe?g|png|gif|svg)$/i);

// styles
import 'bootstrap/dist/css/bootstrap.css';
import './styles/index.styl';

// js
import App from './main';
App();
