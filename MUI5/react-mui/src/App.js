import './App.css';
import TourCard from './components/TourCard.js';
import { Container } from '@mui/material';

function App() {
  return (
    <div className="App">
      <Container>
        <TourCard />
      </Container>
    </div>
  );
}

export default App;
