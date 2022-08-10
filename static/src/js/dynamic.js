odoo.define("elearning_snippet.dynamic", function (require) {
    "use strict";
    console.log("start");
    var publicWidget = require("web.public.widget");
    var ajax = require("web.ajax");
    console.log("running");
    var Dynamic = publicWidget.Widget.extend({
      selector: ".elearn_dynamic",
      start: function () {
        var self = this;
        ajax.jsonRpc("/elearning/snippet", "call", {}).then(function (li) {
          console.log(li[0][0],"test");
         self.$('#course1').text(Object.values(li[0])[0]);
         self.$('#course2').text(Object.values(li[1])[0]);
         self.$('#course3').text(Object.values(li[2])[0]);
          console.log("worked");
        });
      },
    });
    publicWidget.registry.elearning_snippet = Dynamic;
    console.log("end");
    return Dynamic;
  });