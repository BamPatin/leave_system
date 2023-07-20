var allElements = document.getElementsByClassName('DeclineAlert')
Array.from(allElements).forEach(element => {
    element.addEventListener('click', function () {
        var personId = this.getAttribute('data-id');
        Swal.fire({
            //icon: 'warning',
            //title: 'Oops...',
            title: 'Do you want to Decline ?',
            showCancelButton: true,
            cancelButtonText: 'No',
            confirmButtonText: 'Yes, Decline !',
            confirmButtonColor: '#006633',
            cancelButtonColor: '#d33',
            }).then((result) => {
            if (result.isConfirmed) {
                // ปุ่มลบข้อมูลถูกคลิก
                // สามารถเพิ่มโค้ดเพื่อดำเนินการลบข้อมูลได้
                fetch('/unsuccess/' + personId)
                Swal.fire({
                    icon: 'success',
                    title: 'Decline success !',
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


var allElements = document.getElementsByClassName('successAlert')
Array.from(allElements).forEach(element => {
    element.addEventListener('click', function () {
        var personId = this.getAttribute('data-id');
        Swal.fire({
            title: 'Do you want to Approve ?',
            showCancelButton: true,
            cancelButtonText: 'No',
            confirmButtonText: 'Yes, Approve !',
            confirmButtonColor: '#006633',
            cancelButtonColor: '#d33',
            }).then((result) => {
            if (result.isConfirmed) {
                // ปุ่มลบข้อมูลถูกคลิก
                // สามารถเพิ่มโค้ดเพื่อดำเนินการลบข้อมูลได้
                fetch('/success/' + personId)
                Swal.fire({
                    icon: 'success',
                    title: 'Approve success !',
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

