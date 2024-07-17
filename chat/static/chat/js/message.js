const inputField = document.getElementById('textmessageid');
const sendButton = document.getElementById('sendbutton');
const messageList = document.getElementById('messagelist');
const errormessageField = document.getElementById('errormessage');
const inputForm = document.getElementById('chat-form');

sendButton.disabled = true;


function toggleButtonState() {
    inputField.value.trim() ? sendButton.disabled = false : sendButton.disabled = true;
}


function onSubmit(event) {
    event.preventDefault();
    sendButton.disabled = true;
    const name = firstName ? firstName : username;
    const message = inputField.value.trim();
    const time = new Date().getTime();
    const tempMessageId = `temp-${time}`;
    messageList.innerHTML += getMessage(tempMessageId, name, message);
    inputField.value = '';
    onSendMessage(tempMessageId, message);
}

function getMessage(tempMessageId, name, message) {
    return `
    <li class="grey" id="${tempMessageId}">
    <b><span class="msg-date">${formatDate(new Date())}</span>${name}:</b>
    <i>${message}</i>
    </li>
    `
}


async function onSendMessage(tempMessageId, message) {
    const url = "/chat/";
    const tempMessage = document.getElementById(tempMessageId);
    try {
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: createFormData(message)
        })
        let parsedMessage = JSON.parse(await response.json());
        let messageObj = parsedMessage.fields;
        // dont need to do anything now as the message already showing up right!
        tempMessage.classList.remove('grey');
    } catch (e) {
        tempMessage.classList.remove('grey');
        tempMessage.classList.add('red');
        tempMessage.remove();
        console.error("An error occurred: ", e);
    }
    clearUp();
}

function formatDate(dateStr) {
    const date = new Date(dateStr);
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const day = days[date.getUTCDay()];
    const dayOfMonth = date.getUTCDate().toString().padStart(2, '0');
    const month = months[date.getUTCMonth()];

    return `${day} ${dayOfMonth} ${month}`;
}

function clearUp() {
    inputField.value = '';
    const parent = inputField.parentElement;
    if (parent) {
        parent.classList.remove('is-dirty');
    }
    sendButton.disabled = false;
}

function createFormData(message) {
    const formData = new URLSearchParams();
    formData.append('textmessage', message);
    formData.append('csrfmiddlewaretoken', csrftoken);
    return formData.toString();
}

inputField.addEventListener("input", toggleButtonState);

window.addEventListener("online", () => {
    inputForm.hidden = false;
    errormessageField.hidden = true;
})
window.addEventListener("offline", () => {
    inputForm.hidden = true;
    errormessageField.hidden = false;
})
