function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin',
        body: JSON.stringify({ noteId: noteId }),
    }).then(res => {
        if (res.ok) {
            window.location.href = "/";
        }
    })
}

function editNote(noteId) {
    const newData = prompt('Edit your note:');
    if (newData === null) return;
    fetch('/edit-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin',
        body: JSON.stringify({ noteId: noteId, data: newData }),
    }).then((_res) => {
        window.location.href = "/";
    })
}
const successFlashes = document.querySelectorAll('.flash.success');
successFlashes.forEach((flash) => {
    window.setTimeout(() => {
        flash.style.display = 'none';
    }, 2000);
});