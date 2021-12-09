$(function() {
    $(".navbar-toggler").on("click", function(e) {
        $(".tm-header").toggleClass("show");
        e.stopPropagation();
      });
    
      $("html").click(function(e) {
        var header = document.getElementById("tm-header");
    
        if (!header.contains(e.target)) {
          $(".tm-header").removeClass("show");
        }
      });
    
      $("#tm-nav .nav-link").click(function(e) {
        $(".tm-header").removeClass("show");
      });
      setActive();
});
function setActive(){
  let url=decodeURI($(window).attr('location')).split('/')
  let page=url[url.length-1];
  page = page.split('?')[0]
  if(page=='home'){
    $('#tm-nav').find('.active').removeClass('active');
    $('#tm-nav li:eq(0)').addClass("active");
  }else if(page=='about'){
    $('#tm-nav').find('.active').removeClass('active');
    $('#tm-nav li:eq(2)').addClass("active");
  }else if(page=='contact'){
    $('#tm-nav').find('.active').removeClass('active');
    $('#tm-nav li:eq(3)').addClass("active");
  }else if(page=='post'){
    $('#tm-nav').find('.active').removeClass('active');
    $('#tm-nav li:eq(1)').addClass("active");
  }
}