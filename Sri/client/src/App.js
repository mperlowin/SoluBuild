import logo from './logo.svg';
import './App.css';
import LandingPage from './components/LandingPage';
import Layout from './components/Layout';

function App() {
  return (
    <div className="App">
      <Layout>
      <LandingPage />
      </Layout>
    </div>
  );
}

export default App;
