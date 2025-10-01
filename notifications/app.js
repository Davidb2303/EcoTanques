require("dotenv").config();
const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");

const notificationRoutes = require("./routes/notificationRoutes");

const app = express();
const PORT = process.env.PORT || 3001;

app.use(cors());
app.use(bodyParser.json());
app.use("/api/notifications", notificationRoutes);

app.listen(PORT, () => {
  console.log(`Servicio de notificaciones corriendo en el puerto ${PORT}`);
});
