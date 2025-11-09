export interface User {
  email: string;
  name: string;
  picture: string;
}

export interface AuthResponse {
  authenticated: boolean;
  user?: User;
}

export interface LogoutResponse {
  message: string;
}

