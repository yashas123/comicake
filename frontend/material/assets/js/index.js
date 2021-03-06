/* global require ga */
/**
 * Main application entry point
 */
//import Turbolinks from "turbolinks";

import "@stimulus/polyfills";
import { Application } from "stimulus";
import { definitionsFromContext } from "stimulus/webpack-helpers";
import { onLoadMDC } from "./mdc";

const application = Application.start();
const context = require.context("./controllers", true, /\.js$/);
application.load(definitionsFromContext(context));

document.addEventListener("DOMContentLoaded",function(){
    onLoadMDC();
});

// Check that service workers are registered
if ("serviceWorker" in navigator && !window.comicake.DEBUG) {
// Use the window load event to keep the page load performant
    window.addEventListener("load", () => {
        navigator.serviceWorker.register("/sw.js").then(reg => {
            console.log("SW registered: ", reg);
        }).catch(registrationError => {
            console.error("SW registration failed: ", registrationError);
        });
    });
}

//Turbolinks.start(); TODO: why not working!!
/* Take care of Google Analytics page views with turbolinks */
document.addEventListener("turbolinks:load", function(event) {
    onLoadMDC();
    if (typeof ga === "function") { // GA exists
        ga("set", "location", event.data.url);
        ga("send", "pageview");
    }
});