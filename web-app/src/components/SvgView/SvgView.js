import {VelocityComponent} from 'velocity-react';

function SvgView(props) {
  return (
    <VelocityComponent>
      {props.children}
    </VelocityComponent>
  );
}

export default SvgView;