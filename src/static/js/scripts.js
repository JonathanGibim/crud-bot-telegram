function hideFlash() {
	setTimeout(() => {
		const obj = document.querySelector('#modalMessage')
		obj.className += ' hide'
	} , 3000)
}
hideFlash()

function excluir_item(nome_recurso, id_item) {
    swal({
        title: 'Excluir',
        text: 'Tem certeza que deseja excluir este item?',
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, excluir!',
        cancelButtonText: 'Não',
        confirmButtonClass: "btn btn-primary",
        cancelButtonClass: "btn btn-danger",
        buttonsStyling: false
    }).then((result) => {
        if (result.value) {
            xhr = new XMLHttpRequest();
            xhr.open('DELETE', '/' + nome_recurso + '/' + id_item + '/');
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xhr.onload = function() {
                if (xhr.readyState !== 4) return;
                if (xhr.status === 200) {
                    window.location.reload();
                } else {
                    alert('Erro ' + xhr.status);
                }
            };
            xhr.send();
        }
    });
}