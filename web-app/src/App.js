import { useState, memo } from 'react';

import config from './config'
import rect from './assets/rect.svg'
import './App.css';
import SvgView from './components/SvgView/SvgView';
import MqttClient from './services/mqtt/client';

const mqttClient = new MqttClient(config.mqtt, ['sdtest/random/number']);

function App() {
  const [currentNumber, setCurrentNumber] = useState();

  mqttClient.client.onMessageArrived = (message) => {
    setCurrentNumber(message.payloadString);
  };
  
  return (
    <div className="App">
      <span><strong>Current Number</strong>: {currentNumber}</span>
      <SvgView><img src={rect} alt="Rectangle" /></SvgView>
    </div>
  );
}

export default memo(App);
