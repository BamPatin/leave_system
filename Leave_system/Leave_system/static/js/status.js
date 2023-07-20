
var allElements = document.getElementsByClassName('cancelAlert')
Array.from(allElements).forEach(element => {
    element.addEventListener('click', function () {
        var personId = this.getAttribute('data-id');
        Swal.fire({
            icon: 'warning',
            title: 'Oops...',
            text: 'Are you sure you want to delete this form ?',
            showCancelButton: true,
            cancelButtonText: 'No',
            confirmButtonText: 'Yes, Delete it !',
            confirmButtonColor: '#006633',
            cancelButtonColor: '#d33',
            }).then((result) => {
            if (result.isConfirmed) {
                // ปุ่มลบข้อมูลถูกคลิก
                // สามารถเพิ่มโค้ดเพื่อดำเนินการลบข้อมูลได้
                fetch('/delete/' + personId)
                Swal.fire({
                    icon: 'success',
                    title: 'Delete success !',
                    text: '',
                    showConfirmButton: false,})
                setTimeout(function(){
                    location.reload()
                }, 5000);
                
     
            } else if (result.dismiss === Swal.DismissReason.cancel) {
                // ปุ่ม Cancel ถูกคลิก
                // สามารถเพิ่มโค้ดเพื่อดำเนินการเมื่อปุ่ม Cancel ถูกคลิกได้
            }
            });
        });
    });


    
// var allElements = document.getElementsByClassName('cancelAlert')
// allElements = Array.from(allElements)
// for (let element = 0; element < allElements.length; element++) {
//     console.log('******')
//     element.addEventListener('click', function () {
//         var personId = this.getAttribute('data-id');
//         Swal.fire({
//             icon: 'warning',
//             title: 'Oops...',
//             text: 'Are you sure you want to delete this form ?',
//             showCancelButton: true,
//             cancelButtonText: 'No',
//             confirmButtonText: 'Yes, Delete it !',
//             confirmButtonColor: '#006633',
//             cancelButtonColor: '#d33',
//             }).then((result) => {
//             if (result.isConfirmed) {
//                 // ปุ่มลบข้อมูลถูกคลิก
//                 // สามารถเพิ่มโค้ดเพื่อดำเนินการลบข้อมูลได้
//                 fetch('/delete/' + personId)
//                 Swal.fire({
//                     icon: 'success',
//                     title: 'Delete success !',
//                     text: '',
//                     showConfirmButton: false,})
//                 setTimeout(function(){
//                     location.reload()
//                 }, 5000);
                
     
//             } else if (result.dismiss === Swal.DismissReason.cancel) {
//                 // ปุ่ม Cancel ถูกคลิก
//                 // สามารถเพิ่มโค้ดเพื่อดำเนินการเมื่อปุ่ม Cancel ถูกคลิกได้
//             }
//             });
//         });
//     };


