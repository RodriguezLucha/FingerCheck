import React, {Component} from 'react';
import {StyleSheet, Text, View, Button} from 'react-native';
import Biometrics from 'react-native-biometrics';


export default class App extends Component{
  componentDidMount() {
    Biometrics.isSensorAvailable()
      .then((biometryType) => {
        if (biometryType === Biometrics.TouchID) {
          console.log('TouchID is supported');
        } else if (biometryType === Biometrics.FaceID) {
          console.log('FaceID is supported');
        } else {
          console.log('Biometrics not supported');
        }
      });
  }

  createKey(){
    console.log('creating key');
    Biometrics.createKeys('Confirm fingerprint')
      .then((publicKey) => {
        console.log(publicKey);
      });
  }

  render() {
    console.log('the state:', this.state);
    return (
      <View style={styles.container}>
        {/* <Button
          onClick={this.createKey}
          style={styles.welcome}>Create Finger Print</Button> */}
        <Button
          onPress={this.createKey}
          title="Press Me"/>
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
