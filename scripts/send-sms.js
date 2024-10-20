// purpose of sms is to remind users when to return
// service ware before they get charged

const twilio = require('twilio');

const accountSid = AC0236c477c9ca6ea8fc07b065cd5bf626; // Replace with your Twilio Account SID
const authToken = d188477337f7a9bfd326e91897f4bbb7; // Replace with your Twilio Auth Token
const client = new twilio(accountSid, authToken);

function sendReminder(userPhoneNumber) {
    client.messages
        .create({
            body: 'Reminder: Please return your reusable plates to the drop-off points on Governors Island!',
            to: +18447797501, // User's phone number
            from: +18447797501 // Your Twilio number
        })
        .then((message) => console.log(`Message sent: ${message.sid}`))
        .catch((error) => console.error(`Error sending message: ${error}`));
}

// Example user phone number
const userPhoneNumber = +18447797501; // Replace with a real phone number
sendReminder(userPhoneNumber);
