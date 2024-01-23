$(document).ready(function () {

  active_link_menu()
  validation()
  tabel_data()
});


function active_link_menu() {
  $('.nav .nav-link a').click(function (e) {
    e.preventDefault();
    $('.nav .nav-link a').removeClass('active');
    $(this).addClass('active');
  });
}


function tabel_data() {
    new DataTable('#tabel_index',{
      scrollX: true,
      autoWidth: true,
      scrollCollapse: true,
      scrollY : "500px"
  });

    new DataTable('#tabel_disposisi',{
      scrollX: true,
      autoWidth: true,
      scrollCollapse: true,
      scrollY : "500px"
    // "searching": false,
    // "dom": 'rtip'
  });

}




function validation() {
  (() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
  })()
}



var li_items = document.querySelectorAll(".accordion_wrap ul li");
var ul = document.querySelector(".accordion_wrap ul");

li_items.forEach(function(item){
	item.addEventListener("click", function(){
		li_items.forEach(function(item){
			item.classList.remove("active");
		})
		item.classList.add("active");
	});
});

ul.addEventListener("mouseleave", function(){
	li_items.forEach(function(item){
		item.classList.remove("active");
	})
});