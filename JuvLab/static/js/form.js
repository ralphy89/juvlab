const save_participant_btn = document.getElementById('save-student-btn');
save_participant_btn.addEventListener('click', async () => {
    const first_name = document.getElementById('first-name');
    const last_name = document.getElementById('last-name');
    const email = document.getElementById('student-email');
    const phone = document.getElementById('student-phone');
    const program = document.getElementById('student-program');
    const dataToSend = {
            'first_name': first_name.value,
            'last_name': last_name.value,
            'email': email.value,
            'phone': parseInt(phone.value),
            'program': program.value,
        }
    ;
    const response = await fetch('http://127.0.0.1:8000/api/add_students', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(dataToSend),
        // …
    });

    if (response.ok) {
        const data = await response.json();
        location.reload();
    }
    document.getElementById('modal-title-h3').innerText = 'Add Participant';
})

function resetForm() {
    // Reset all form fields
    document.querySelectorAll('#student-form-modal input').forEach(input => {
        input.value = '';
    });
}