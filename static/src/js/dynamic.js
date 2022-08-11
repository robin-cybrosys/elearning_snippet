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
      ajax.jsonRpc("/elearning/snippet", "call", {}).then(function (vals) {
        console.log(vals, "test");
        console.log(vals.courses, "test");
        // var items;
        // items = li.forEach(function (item) {
          // console.log(item);
           self.$("#course1").text(vals.courses);
        // });

        // console.log(items, "fdddddddd");
        //  self.$('#course1').text(Object.values(li[0])[0]);
        //  self.$('#course2').text(Object.values(li[1])[0]);
        //  self.$('#course3').text(Object.values(li[2])[0]);
        console.log("worked");
      });
    },
  });
  var originalColors = [];
  console.log(originalColors);
  console.log(Colors);
  var Colors = [];

  // Changes color on hover
  $(function () {
    $(".btn-dp").hover(
      function () {
        originalColors[$(this).index(".btn-dp")] =
          $(this).css("background-color");
        $(this).css("background-color", "#aaaaa");

        Colors[$(this).index(".btn-dp")] = $(this).css("color");
        $(this).css("color", "#fff");
      },
      function () {
        $(this).css(
          "background-color",
          originalColors[$(this).index(".btn-dp")]
        );

        $(this).css("color", Colors[$(this).index(".btn-dp")]);
      }
    );
  });

  publicWidget.registry.elearning_snippet = Dynamic;
  console.log("end");
  return Dynamic;
});
