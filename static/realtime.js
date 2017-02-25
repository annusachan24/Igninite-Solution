"use strict";

function append_to_dom(data) {
    var data = JSON.parse(data)
    if (data.length == 0) {
        return
    }
    //append the contents in div id realtime
    var blocks = data.map(function (art) {
        var block = "<div class='col-sm-4'><div class='card' style='width: 40rem;border-radius:5px;background-color:#3CB371;text-align:center'><div class='container'><h5 class='card-title' style='font-family: 'Playfair Display', serif;'>" + art.Title;
        block += " " + "</h5><p class='card-text' style='margin-top:-15px'>" + " &nbsp  Summary: " + art.Summary + "<br>";
        block += " &nbsp  Link: " + "<a style='color:#d9e534' href='"+ art.URL+"'>"+art.URL + "</a>" + "<br>"
        block +=  "<br></p></div></div><br></div>";
        return block;
    });
	$("#realtime").empty()
    $("#realtime").prepend(blocks);
    $("#realtime").attr("modified", Date.now());
}

function doPoll() {
    $.ajax({
        url: "update",
        data: {
            "timestamp": parseInt($('#realtime').attr("modified") / 1000) || 0
        }
    }).done(function (data) {
        append_to_dom(data);
    }).always(function () {
        setTimeout(doPoll, 5000);
    })
}


$(document).ready(function () {
    doPoll();
})
