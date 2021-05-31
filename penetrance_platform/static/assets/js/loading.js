function showLoading() {
    loadingImg ="<div id='loadingImg'>";
    loadingImg +=" <img src='/static/assets/img/loading_spinner.gif' style='position: relative; display: block; margin: 0px auto;'/>";
    loadingImg +="</div>";

    //화면에 레이어 추가
    $('body').append(loadingImg)

    //마스크의 높이와 너비를 화면 것으로 만들어 전체 화면을 채웁니다.
    $('#loadingImg').css({
         'position': 'absolute',
         'left': '50%',
         'top': '50%',
         'background': '#ffffff'
         });

    //로딩중 이미지 표시
    $('#loadingImg').show();
}

function closeLoading() {
    $('#loadingImg').hide();
    $('#loadingImg').empty();
}