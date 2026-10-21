import axios from 'axios'

const API_URL= 'http://localhost:8000'

const loginUser = async (credentials) => {
  try {
    const params= URLSearchParams();
    for (const key in credentials) {
      params.append(key, credentials[key])

  }
  const response= await axios.post(
    `${API_URL}/auth/token`,
    params,
    {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',

      },
    }
  );

  return response.data

  } catch(error) {
    console.log('Error logging in user;', error);
    throw error
  }

};

const registerUser = async (userData) => {
  try {
    await axios.post(`${API_URL}/auth/register`, userData);

  } catch (error) {
    console.log('Registration Error;', error);
    throw error;

  }
};

const fetchUserProfile = async (token) => {
  try {
    const response= await axios.get(
      `${API_URL}/users/me`,
      {
        headers: {
          'Authorization': `Bearer ${token}`,
        }
      }
    );
    return response.data

  } catch (error) {
    console.log('Error fetching user profile;', error);
    throw error;

  }
};

export {loginUser, registerUser, fetchUserProfile};