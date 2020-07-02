
$(document).ready(function () {
    console.log("로딩 완료");

    $("#corp-finstate").html("");
  });

function searchCorp(){
    let corp = $('#input-corp').val()
    $.ajax({
        type: "POST",
        url: "/report",
        data: {
            corp: corp
        },
        success: function (response) {
            alert("리포트 페이지 요청!");

            $("#corp-name").text(corp);
        }
    });
}

