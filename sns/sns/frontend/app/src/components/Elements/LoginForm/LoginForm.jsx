import { TextField, InputAdornment } from "@mui/material";

export const LoginForm = () => (
    <div>
        <TextField
            id="email"
            label="Email"
            variant="outlined"
            size="small"
            margin="dense"
        />
        <br />
        <TextField
            id="password"
            label="Password"
            variant="outlined"
            size="small"
            margin="dense"
            type="password"
        />
    </div>
);
