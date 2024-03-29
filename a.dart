import 'dart:math';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:easy_vahan/common/data_store.dart';
import 'package:easy_vahan/models/car.dart';
import 'package:easy_vahan/providers/user_info.dart';
import 'package:easy_vahan/providers/car_info.dart';
import 'package:easy_vahan/screens/add_ev/repo/car_repo.dart';
import 'package:flutter/material.dart';
import 'package:easy_vahan/models/user.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:easy_vahan/common/navigation.dart';
import 'package:easy_vahan/common/routing.dart';

class AddCarViewModel extends ChangeNotifier {
  final CarRepo myRepo;
  final DataStore store;
  final UserProv userProvider;
  final CarProv carProv;

  AddCarViewModel(
      {required this.store,
      required this.myRepo,
      required this.userProvider,
      required this.carProv});

  String _number = "";
  String _capacity = "";
  String _company = "";
  String _model = "";
  String _carName = "";

  get number => _number;

  get capacity => _capacity;

  get company => _company;

  get model => _model;

  get carName => _carName;

  setNumber(String value) {
    _number = value;
  }

  setCapacity(String value) {
    _capacity = value;
  }

  setCompany(String value) {
    _company = value;
  }

  setModel(String value) {
    _model = value;
  }

  setCarName(String value) {
    _carName = value;
  }

  bool _loading = false;

  bool get loading => _loading;

  setLoading(bool value) {
    _loading = value;
    notifyListeners();
  }

  bool _detailVisible = false;

  bool get detailVisible => _detailVisible;

  void toggleVisible() {
    _detailVisible = !_detailVisible;
    notifyListeners();
  }

  String errorText = "";

  void clearValues() {
    _number = "";
    _capacity = "";
    _company = "";
    _model = "";
    _carName = "";
  }

  String removeNonNumericCharacters(String input) {
    return input.replaceAll(RegExp(r'[^0-9]'), '');
  }

  String generateID() {
    var id = DateTime.now();
    var i = id.toString();
    i = removeNonNumericCharacters(i);
    BigInt n = BigInt.parse(i);
    String fi = n.toRadixString(24);
    return fi;
  }

  Future<void> addCarToDB(BuildContext context) async {
    FirebaseFirestore firebaseFirestore = FirebaseFirestore.instance;
    UserModel userModel = userProvider.getUserInfo();

    var intValue = Random().nextInt(26) + 1;

    Map data = {
      'number': _number.trim(),
      'capacity': _capacity,
      'company': _company.trim(),
      'model': _model.trim(),
      'carName': _carName.trim(),
      'dp': intValue,
    };

    setLoading(true);

    try {
      var carId = generateID();
      CarModel carModel = CarModel(
          carID: carId,
          number: data['number'],
          capacity: data['capacity'],
          company: data['company'],
          model: data['model'],
          carName: data['carName'],
          dp: data['dp']);
      // print(carModel.carID);
      // print(userModel.email);
      // await firebaseFirestore
      //     .collection("users")
      //     .doc(userModel.uid)
      //     .collection('cars')
      //     .doc(carId)
      //     .set(carModel.toJson());

      setLoading(false);

      //   await Navigator.of(NavigationService.navigatorKey.currentContext!,
      //           rootNavigator: true)
      //       .pushAndRemoveUntil(
      //           Routes.testing(), (Route<dynamic> route) => false);
    } catch (e) {
      Fluttertoast.showToast(
          msg: e.toString(),
          toastLength: Toast.LENGTH_LONG,
          backgroundColor: Colors.red);
    }
  }
}