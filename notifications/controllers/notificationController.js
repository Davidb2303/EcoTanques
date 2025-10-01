const { sendPushNotification } = require("../services/fcmService");

const sendNotification = async (req, res) => {
  const { token, title, body, data } = req.body;

  try {
    const response = await sendPushNotification(token, title, body, data);
    res.status(200).json({ success: true, messageId: response });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};

module.exports = {
  sendNotification,
};
