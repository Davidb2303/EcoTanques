const admin = require("../config/firebaseConfig");

const sendPushNotification = async (token, title, body, data = {}) => {
  const message = {
    notification: {
      title,
      body,
    },
    data,
    token,
  };

  return await admin.messaging().send(message);
};

module.exports = {
  sendPushNotification,
};
