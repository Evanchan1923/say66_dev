$(document).ready(function () {
    // Send text input to the API
    $('#sendText').click(function () {
        const textInput = $('#textInput').val();
        if (!textInput) {
            alert('Please enter some text!');
            return;
        }

        const formData = new FormData();
        formData.append('text', textInput);

        $.ajax({
            url: '/api/respond',
            method: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (response) {
                $('#responseText').text(`Input: ${response.input}, Response: ${response.response}`);
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.error || "Unknown error occurred.";
                $('#responseText').text(`Error: ${errorMsg}`);
            }
        });
    });

    // Send audio input to the API
    $('#sendAudio').click(function () {
        const audioInput = $('#audioInput')[0].files[0];
        if (!audioInput) {
            alert('Please select an audio file!');
            return;
        }

        const formData = new FormData();
        formData.append('audio', audioInput);

        $.ajax({
            url: '/api/respond',
            method: 'POST',
            processData: false,
            contentType: false,
            data: formData,
            success: function (response) {
                $('#responseText').text(`Input: ${response.input}, Response: ${response.response}`);
            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.error || "Unknown error occurred.";
                $('#responseText').text(`Error: ${errorMsg}`);
            }
        });
    });
});
