import rect from './assets/rect.svg'
import './App.css';
import SvgView from './components/SvgView/SvgView';

function App() {
  return (
    <div className="App">
      <SvgView><img src={rect} alt="Rectangle" /></SvgView>
    </div>
  );
}

export default App;
