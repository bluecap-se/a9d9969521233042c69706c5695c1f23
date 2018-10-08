$(function() {

    var userHasVoted = false,
        voteId = null;

    $("#formCastVote").on("submit", function(e){
        e.preventDefault();

        var ajaxCall, type,
            url = this.action;

        type = (userHasVoted === true) ? "put" : "post";
        url += (voteId !== null) ? "/" + voteId : "";

        ajaxCall = $.ajax({url: url, type: type, data: $(this).serialize()});

        ajaxCall.done(function(data) {
            userHasVoted = true;
            voteId = data["id"];

            $("#usernameInput").attr("readonly", true);
        });
    });

    var getParticipantsList = function() {
        var ajaxCall = $.get("/view-participants?poll=" + pollId),
            $container = $("#participantsContainer");

        ajaxCall.done(function(data) {
            if (data.length > 0) {
                $container.html(""); // empty the container
            }

            var i = 0, $list = $("<div>"), $el, name, vote;

            for (; i < data.length; i++) {
                name = data[i]["username"];
                vote = data[i]["vote"] === null ? "No vote" : data[i]["vote"];

                if (data[i]["id"] === voteId) {
                    name = "(you) " + name;
                }

                $el = $("<p>").html(name + ": " + vote);

                $list.append($el);
            }

            $container.append($list);
        });
    };

    // Fetch participants once every other sec
    setInterval(getParticipantsList, 2000);
    getParticipantsList();

});
