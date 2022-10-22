import { Button } from "@mui/material";
import styled from "styled-components";

const StyleMargin = styled.div`
    margin: 15px;
`;

export const RichButton = (props) => {
    return (
        <StyleMargin>
            <Button
                variant="outlined"
                size="small"
                margin="dense"
                onClick={props.onClick}
            >
                {props.type}
            </Button>
        </StyleMargin>
    );
};
