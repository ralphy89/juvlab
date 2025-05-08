const save_participant_btn = document.getElementById('save-student-btn');
const save_computer_btn = document.getElementById('save-computer-btn');

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
save_computer_btn.addEventListener('click', async () => {
    const host_name = document.getElementById('pc-name');
    const pc_model = document.getElementById('pc-model');
    const mac = document.getElementById('pc-mac');
    const status = document.getElementById('pc-status');
    const dataToSend = {
            'host_name': host_name.value,
            'mac_adr': mac.value,
            'pc_model': pc_model.value,
            'status': status.value,
        };
    const response = await fetch('http://127.0.0.1:8000/api/add_computers', {
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
})

function resetForm() {
    // Reset all form fields
    document.querySelectorAll('#student-form-modal input').forEach(input => {
        input.value = '';
    });
}