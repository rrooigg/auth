import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';

import AuthProvider from './context/AuthContent.jsx';
import Register from './components/Register.jsx';
import Login from './components/Login.jsx';
import UserProfile from './components/UserProfile.jsx';

import './App.css'

function App() {
  return (
    <Router>
      <AuthProvider>
        <div style={{ 'padding': '20px'}}>
          <nav>
            <ul>
              <li><Link>Register</Link></li>
              <li><Link>Login</Link></li>
              <li><Link>Profile</Link></li>
            </ul>
          </nav>
          <Routes>
            <Route path='/register' element={<Register/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/profile' element={<UserProfile/>}/>
          </Routes>
        </div>

      </AuthProvider>
    </Router>
 
  );
};

export default App
