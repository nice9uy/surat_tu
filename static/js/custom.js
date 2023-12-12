$(document).ready(function () {
  active_link_menu()
  validation()
  tabel_data()
  // table_surat_keluar()
});


function active_link_menu() {
  $('.nav .nav-link a').click(function (e) {
    e.preventDefault();
    $('.nav .nav-link a').removeClass('active');
    $(this).addClass('active');
  });
}

function tabel_data(){
  new DataTable('#tabel_index');
  new DataTable('#tabel_surat_keluar', {
    "searching": false,
    "dom": 'rtip',
  //   fixedColumns: {
  //     left: 4,
     
  // },
//   //   paging: false,
//   fixedColumns: {
//     left: 2
// },
    scrollCollapse: true,
    scrollX: true,
    autoWidth: true,
    // overflow-y: auto;
  //   // scrollY: 300


  });
  new DataTable('#tabel_klasifikasi',{
    "searching": false,
    "dom": 'rtip'
  });
  new DataTable('#tabel_subklasifikasi' , {
    "searching": false,
    "dom": 'rtip'
  });
}

// function table_surat_keluar(){
//   var table = $('#tabel_surat_keluar').DataTable({
//     // Your DataTables options go here
//     });
//   new $.fn.dataTable.FixedColumns(table, {
//     leftColumns: 1,  // Number of columns to fix on the left
//     rightColumns: 1  // Number of columns to fix on the right
// });

  
// }

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

