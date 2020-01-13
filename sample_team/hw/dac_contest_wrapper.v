//Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2018.2 (lin64) Build 2258646 Thu Jun 14 20:02:38 MDT 2018
//Date        : Tue May 14 11:30:13 2019
//Host        : goeders-ssh0 running 64-bit Ubuntu 16.04.6 LTS
//Command     : generate_target dac_contest_wrapper.bd
//Design      : dac_contest_wrapper
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module dac_contest_wrapper
   (bt_ctsn,
    bt_rtsn,
    gpio_sensors_tri_io,
    uart0_ctsn,
    uart0_rtsn,
    uart0_rxd,
    uart0_txd,
    uart1_rxd,
    uart1_txd);
  input bt_ctsn;
  output bt_rtsn;
  inout [5:0]gpio_sensors_tri_io;
  input uart0_ctsn;
  output uart0_rtsn;
  input uart0_rxd;
  output uart0_txd;
  input uart1_rxd;
  output uart1_txd;

  wire bt_ctsn;
  wire bt_rtsn;
  wire [0:0]gpio_sensors_tri_i_0;
  wire [1:1]gpio_sensors_tri_i_1;
  wire [2:2]gpio_sensors_tri_i_2;
  wire [3:3]gpio_sensors_tri_i_3;
  wire [4:4]gpio_sensors_tri_i_4;
  wire [5:5]gpio_sensors_tri_i_5;
  wire [0:0]gpio_sensors_tri_io_0;
  wire [1:1]gpio_sensors_tri_io_1;
  wire [2:2]gpio_sensors_tri_io_2;
  wire [3:3]gpio_sensors_tri_io_3;
  wire [4:4]gpio_sensors_tri_io_4;
  wire [5:5]gpio_sensors_tri_io_5;
  wire [0:0]gpio_sensors_tri_o_0;
  wire [1:1]gpio_sensors_tri_o_1;
  wire [2:2]gpio_sensors_tri_o_2;
  wire [3:3]gpio_sensors_tri_o_3;
  wire [4:4]gpio_sensors_tri_o_4;
  wire [5:5]gpio_sensors_tri_o_5;
  wire [0:0]gpio_sensors_tri_t_0;
  wire [1:1]gpio_sensors_tri_t_1;
  wire [2:2]gpio_sensors_tri_t_2;
  wire [3:3]gpio_sensors_tri_t_3;
  wire [4:4]gpio_sensors_tri_t_4;
  wire [5:5]gpio_sensors_tri_t_5;
  wire uart0_ctsn;
  wire uart0_rtsn;
  wire uart0_rxd;
  wire uart0_txd;
  wire uart1_rxd;
  wire uart1_txd;

  dac_contest dac_contest_i
       (.bt_ctsn(bt_ctsn),
        .bt_rtsn(bt_rtsn),
        .gpio_sensors_tri_i({gpio_sensors_tri_i_5,gpio_sensors_tri_i_4,gpio_sensors_tri_i_3,gpio_sensors_tri_i_2,gpio_sensors_tri_i_1,gpio_sensors_tri_i_0}),
        .gpio_sensors_tri_o({gpio_sensors_tri_o_5,gpio_sensors_tri_o_4,gpio_sensors_tri_o_3,gpio_sensors_tri_o_2,gpio_sensors_tri_o_1,gpio_sensors_tri_o_0}),
        .gpio_sensors_tri_t({gpio_sensors_tri_t_5,gpio_sensors_tri_t_4,gpio_sensors_tri_t_3,gpio_sensors_tri_t_2,gpio_sensors_tri_t_1,gpio_sensors_tri_t_0}),
        .uart0_ctsn(uart0_ctsn),
        .uart0_rtsn(uart0_rtsn),
        .uart0_rxd(uart0_rxd),
        .uart0_txd(uart0_txd),
        .uart1_rxd(uart1_rxd),
        .uart1_txd(uart1_txd));
  IOBUF gpio_sensors_tri_iobuf_0
       (.I(gpio_sensors_tri_o_0),
        .IO(gpio_sensors_tri_io[0]),
        .O(gpio_sensors_tri_i_0),
        .T(gpio_sensors_tri_t_0));
  IOBUF gpio_sensors_tri_iobuf_1
       (.I(gpio_sensors_tri_o_1),
        .IO(gpio_sensors_tri_io[1]),
        .O(gpio_sensors_tri_i_1),
        .T(gpio_sensors_tri_t_1));
  IOBUF gpio_sensors_tri_iobuf_2
       (.I(gpio_sensors_tri_o_2),
        .IO(gpio_sensors_tri_io[2]),
        .O(gpio_sensors_tri_i_2),
        .T(gpio_sensors_tri_t_2));
  IOBUF gpio_sensors_tri_iobuf_3
       (.I(gpio_sensors_tri_o_3),
        .IO(gpio_sensors_tri_io[3]),
        .O(gpio_sensors_tri_i_3),
        .T(gpio_sensors_tri_t_3));
  IOBUF gpio_sensors_tri_iobuf_4
       (.I(gpio_sensors_tri_o_4),
        .IO(gpio_sensors_tri_io[4]),
        .O(gpio_sensors_tri_i_4),
        .T(gpio_sensors_tri_t_4));
  IOBUF gpio_sensors_tri_iobuf_5
       (.I(gpio_sensors_tri_o_5),
        .IO(gpio_sensors_tri_io[5]),
        .O(gpio_sensors_tri_i_5),
        .T(gpio_sensors_tri_t_5));
endmodule
